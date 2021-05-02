from matplotlib import pyplot as plt
from face_mask_detector import FaceMaskDetector
from parameters import (
    DATA_DIR,
    SAVE_DIR,
    VAL_SPLIT,
    SEED,
    BATCH_SIZE,
    IMG_WIDTH,
    IMG_HEIGHT,
    CLASS_NAMES,
    EPOCHS,
)

mask_detector = FaceMaskDetector(
    class_names=CLASS_NAMES,
    model_path=None,
    data_dir=DATA_DIR,
    val_split=VAL_SPLIT,
    seed=SEED,
    img_height=IMG_HEIGHT,
    img_width=IMG_WIDTH,
    batch_size=BATCH_SIZE,
    epochs=EPOCHS,
)
mask_detector.save_model(SAVE_DIR)
history = mask_detector.history
acc = history.history["accuracy"]
val_acc = history.history["val_accuracy"]

loss = history.history["loss"]
val_loss = history.history["val_loss"]

epochs_range = range(EPOCHS)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label="Training Accuracy")
plt.plot(epochs_range, val_acc, label="Validation Accuracy")
plt.legend(loc="lower right")
plt.title("Training and Validation Accuracy")

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label="Training Loss")
plt.plot(epochs_range, val_loss, label="Validation Loss")
plt.legend(loc="upper right")
plt.title("Training and Validation Loss")
plt.show()
