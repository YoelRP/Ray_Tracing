if(self.preview_obj != [] and self.preview_image !=[]):
    recalculete_obj = []
        for i in range(self.cant_Obj):
            if(self.preview_obj[i].compare(scene.obj[i])):
                recalculete_obj.append(scene.obj[i].id)
        for j in range(height):
            y = y0 + j * ystep
            for i in range(width):
                x = x0 + i * xstep
                if(recalculete_obj in preview_objects_hit_pixel[i][j]):
                    ray = Ray(camera, Point(x, y) - camera)
                    pixels.set_pixel(i, j, self.ray_trace(ray, scene, i, j))
                    self.cant_ray= self.cant_ray +1
                else:
                    pixels.set_pixel(i, j, preview_image[i][j]
else: