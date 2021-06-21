from image import Image
from ray import Ray
from point import Point
from color import Color
from vector import Vector
import numpy as np


class RenderEngine:
    def __init__(self, width, height, cant_Obj, preview_obj=[], preview_objects_hit_pixel=[], preview_image=[], cant_ray=0, MAX_DEPTH=5, MIN_DISPLACE=0.0001):
        self.height = height
        self.width = width
        self.cant_Obj = cant_Obj
        self.cant_rays = 0
        self.preview_objects_hit_pixel = preview_objects_hit_pixel
        self.actual_objects_hit_pixel = [
            [[]for _ in range(height)]for _ in range(width)]
        self.first_frame = True
        self.preview_obj = preview_obj
        self.MAX_DEPTH = MAX_DEPTH
        self.MIN_DISPLACE = MIN_DISPLACE
        self.cant_ray = cant_ray
        self.preview_image = preview_image

    def render(self, scene):
        self.cant_ray = 0
        width = scene.width
        height = scene.height
        aspect_ratio = float(width) / height
        x0 = -1.0
        x1 = +1.0
        xstep = (x1 - x0) / (width - 1)
        # print("xstep"+str(xstep))

        y0 = -1.0 / aspect_ratio
        y1 = +1.0 / aspect_ratio
        ystep = (y1 - y0) / (height - 1)
        # print("ystep"+str(ystep))

        close_pixels = 10
        half_closepixels = close_pixels/2
        camera = scene.camera
        pixels = Image(width, height)
        pixels_render = np.zeros((width+5, height+5))
        if(self.preview_obj != [] and self.preview_image != []):
            recalculete_obj = []
            for i in range(self.cant_Obj):
                if(not(self.preview_obj[i].compare(scene.objects[i]))):
                    recalculete_obj.append(scene.objects[i].id)
            if(recalculete_obj==[]):
                return self.preview_image
            for j in range(height):
                y = y0 + j * ystep
                for i in range(width):
                    x = x0 + i * xstep
                    for m in range(len(recalculete_obj)):
                        if(recalculete_obj[m] in self.preview_objects_hit_pixel[i][j]):
                            for k in range(close_pixels):
                                for l in range(close_pixels):
                                    if(i-5+l < width and j-5+l < height and (i-5+l) >= 0 and j-5+l >= 0):
                                        if(pixels_render[(i-5+l)][(j-5+l)] == 0):
                                            ray = Ray(camera, Point(x, y) - camera)
                                            pixels.set_pixel(
                                                i, j, self.ray_trace(ray, scene, i-5+l, j-5+k))
                                            self.cant_ray = self.cant_ray + 1
                                            pixels_render[i-5+l][j-5+k] = 1
                        else:
                            pixels.set_pixel(i, j, Color(0, 0, 0))
        else:
            for j in range(height):
                y=y0 + j * ystep
                for i in range(width):
                    x=x0 + i * xstep
                    ray=Ray(camera, Point(x, y) - camera)
                    pixels.set_pixel(i, j, self.ray_trace(ray, scene, i, j))
                    self.cant_ray = self.cant_ray + 1
                # print("{:3.0f}%".format(float(j)/float(height)*100), end="\r")
        self.preview_objects_hit_pixel=self.actual_objects_hit_pixel
        self.preview_obj=scene.objects
            
        return pixels

    def ray_trace(self, ray, scene, x, y, depth=0):
        color=Color(0, 0, 0)
        dist_hit, obj_hit=self.find_nearest(ray, scene)
        # print(x)
        if obj_hit is None:
            return color

        if(obj_hit.id not in self.actual_objects_hit_pixel):
            # print(x)
            # print(self.actual_objects_hit_pixel[x-1])
            self.actual_objects_hit_pixel[x][y].append(obj_hit.id)
        hit_pos=ray.origin + ray.direction * dist_hit

        hit_normal=obj_hit.normalf(hit_pos)
        color += self.color_at(obj_hit, hit_pos, hit_normal, scene)
        if depth < self.MAX_DEPTH:
            new_ray_pos=hit_pos+hit_normal * self.MIN_DISPLACE
            new_ray_dir=ray.direction - 2 * \
                ray.direction.dot_product(hit_normal) * hit_normal
            new_ray=Ray(new_ray_pos, new_ray_dir)
            # new color with the reflected cofficient
            color += self.ray_trace(new_ray, scene, x,
                                    y, depth+1)*obj_hit.material.reflection
        return color

    def find_nearest(self, ray, scene):
        dist_min=None
        obj_hit=None
        for obj in scene.objects:
            dist=obj.intersects(ray)
            if dist is not None and (obj_hit is None or dist < dist_min):
                dist_min=dist
                obj_hit=obj
        return (dist_min, obj_hit)

    def color_at(self, obj_hit, hit_pos, normal, scene):
        material=obj_hit.material
        obj_color=material.color_at(hit_pos)
        to_cam=scene.camera - hit_pos
        specular_k=50
        color=material.ambient * Color.from_hex("#FFFFFF")
        for light in scene.lights:
            to_light=Ray(hit_pos, light.position - hit_pos)
            # difuese
            color += (obj_color * material.diffuse * \
                      max(normal.dot_product(to_light.direction), 0))
            # specular shading
            half_vector=(to_light.direction + to_cam).normalize()
            color += (light.color * material.specular * \
                      max(normal.dot_product(half_vector), 0)**specular_k)
        return color
