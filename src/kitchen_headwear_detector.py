# Kitchen Headwear & Hairnet Compliance Monitor
import cv2

def verify_hairnet_compliance(person_box, headwear_box):
    # Headwear must lie within the upper 40% of person bounding box
    px1, py1, px2, py2 = person_box
    hx1, hy1, hx2, hy2 = headwear_box
    
    head_region_bottom = py1 + (py2 - py1) * 0.40
    headwear_center_y = (hy1 + hy2) / 2
    headwear_center_x = (hx1 + hx2) / 2
    
    is_in_head_zone = (py1 <= headwear_center_y <= head_region_bottom)
    is_horizontally_aligned = (px1 <= headwear_center_x <= px2)
    return is_in_head_zone and is_horizontally_aligned

if __name__ == "__main__":
    print("Kitchen Headwear Compliance Verifier initialized.")
