""" This is a code snippet for showing the images which the model predicted incorrectly and it's correct label
 and predicted label in the image classification problem """
import torch
import matplotlib.pyplot as plt

def detect_wrong_preds(model, val_loader, dataset):
  for batch in val_loader:
    imgs, labels = batch
    # generate the prediction
    out = model(imgs) 
    # get the max probabilty class
    _, preds = torch.max(out, dim=1)
    got = preds == labels
    for i in range(len(got)):
      if not got[i]:
        plt.imshow(imgs[i].permute(1, 2, 0).cpu().detach().numpy())
        plt.show()
        print('Label:', dataset.classes[labels[i]], ', Predicted:', dataset.classes[preds[i]])
    break