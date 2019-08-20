from utils.image_utils import image_saver

is_vehicle_detected = [0]
bottom_position_of_detected_vehicle = [0]
left_position_of_detected_vehicle = [0]
last_frame_is_vehicle_detected = [0]

def count_objects_x_axis(top, bottom, right, left, crop_img, roi_position, y_min, y_max, deviation,roiArea):   
        direction = "n.a." # means not available, it is just initialization
        isInROI = True # is the object that is inside Region Of Interest
        update_csv = False

        if (abs(((right+left)/2)-roi_position) < deviation and last_frame_is_vehicle_detected[0] !=1 ):
          is_vehicle_detected.insert(0,1)
          #Added for testing
          last_frame_is_vehicle_detected.insert(0,1)
          update_csv = True
          image_saver.save_image(crop_img) # save detected object image
        else:
                last_frame_is_vehicle_detected.insert(0,0)
                  

        if(left > left_position_of_detected_vehicle[0]):
                direction = "right"
        else:
                direction = "left"
        # This to keep track of last frame detection
        bottom_position_of_detected_vehicle.insert(0,(bottom))
        left_position_of_detected_vehicle.insert(0,(left))

        return direction, is_vehicle_detected, update_csv

