import torchvision as tv
from matplotlib import pyplot as plt
import typer


def download_data():
  dataset = tv.datasets.Cityscapes(
    './data/cityspaces', split='train', mode='fine', target_type='semantic'
  )

  img, smnt = dataset[0]
  plt.imshow(img)
  plt.show()



def main():
  download_data()


if __name__ == '__main__':
  import typer

  typer.run(main)
