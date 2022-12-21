def display_instances(datapoint):
    """
    This function takes a batch from the dataset and display the image with 
    the associated bounding boxes.
    """
    # ADD CODE HEREs
    colors = {
        1:"red", 
        2:"blue", 
        4:"green"
    }
    
    w, h, c = datapoint["image"].shape
    
    
    fig, ax = plt.subplots(figsize=(7,7))
    
    ax.imshow(datapoint["image"].numpy().astype("uint8"))
    
    groundtruth_classes = datapoint["groundtruth_classes"].numpy()
    
    for i in range(len(datapoint["groundtruth_boxes"])):
        ymin, xmin, ymax, xmax = datapoint["groundtruth_boxes"][i]
        ground_class = groundtruth_classes[i]

        rect = matplotlib.patches.Rectangle((xmin*w, ymin*h), (xmax-xmin)*w, (ymax-ymin)*h, 
                                            edgecolor=colors[ground_class], facecolor="none")
        ax.add_patch(rect)
        
    plt.show()
    
    
    for datapoint in dataset.take(10):
    display_instances(datapoint)
    
    
    
    
    
    
    
classes_count = {1: 0, 2: 0, 4: 0}
for batches in dataset.take(10000):
    for gt_cl in batches["groundtruth_classes"].numpy():
        classes_count[gt_cl] += 1

classes_count        




class_name = ['vehicle', 'pedestrian', 'cyclist']
plt.bar(class_name, classes_count.values(), color=['red', 'blue', 'green'])
plt.ylabel('Counts of detected objects')
plt.title('Distribution of 3 classes for 10000 images')