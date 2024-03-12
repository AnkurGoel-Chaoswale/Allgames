import cv2
import uuid
import os

def draw_boxes_and_labels_correct_format(img_path, output_path):
    # Load the image
    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)

    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Thresholding to get the binary image
    _, binary = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)
    
    # Find contours
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Font for the text
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.4
    font_thickness = 1
    
    # Process each contour
    for contour in contours:
        # Get the bounding box coordinates
        x, y, w, h = cv2.boundingRect(contour)
        
        # Draw the bounding box
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 1)
        
        # Prepare the dimension text
        dimension_text = f"{w}*{h}"
        # Prepare the coordinate text
        coordinate_text = f"{x},{y}"
        print(dimension_text,"       ",coordinate_text)
        # Get the size of the dimension text
        dimension_text_size, _ = cv2.getTextSize(dimension_text, font, font_scale, font_thickness)
        coordinate_text_size, _ = cv2.getTextSize(coordinate_text, font, font_scale, font_thickness)

        # Calculate the position for the dimension text background
        dimension_bg_from = (x + 1, y + 1)
        dimension_bg_to = (x + dimension_text_size[0] + 2, y + dimension_text_size[1] + 2)
       

        # Calculate the position for the coordinate text background
        coordinate_bg_from = (x + w - coordinate_text_size[0] - 3, y + h - coordinate_text_size[1] - 3)
        coordinate_bg_to = (x + w - 1, y + h - 1)
       
        

        # Draw the background for dimension and coordinate text
        cv2.rectangle(img, dimension_bg_from, dimension_bg_to, (255, 255, 255), -1)
        cv2.rectangle(img, coordinate_bg_from, coordinate_bg_to, (255, 255, 255), -1)
        
        # Put the dimension text
        cv2.putText(img, dimension_text, (x + 1, y + dimension_text_size[1] + 1), font, font_scale, (0, 0, 0), font_thickness)
        
        # Put the coordinate text
        cv2.putText(img, coordinate_text, (x + w - coordinate_text_size[0] - 2, y + h - 2), font, font_scale, (0, 0, 0), font_thickness)
        
    # Save the processed image
    cv2.imwrite(output_path, img)
    
    return output_path
import uuid

# Generate a UUID
curr = str(uuid.uuid4())

input_image_path = "C:/Users/DELL/Downloads/aaaa.jpeg"
output_directory = f"C:/Users/DELL/Desktop/chaotics/{curr}.png"
output_image_path = draw_boxes_and_labels_correct_format(input_image_path, output_directory)
print("Image saved as:", output_image_path)