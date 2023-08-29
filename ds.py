class docusketch_test:

  def read_json(self, path):
    import pandas as pd
    try:
      df = pd.read_json(path)
    except ValueError:
      print('Are you sure that your path is to json-file?')
    return df

  def show_plots(self):
    try:
      df = self.read_json(path)
      df.hist(layout=(-1, 6), figsize=(16,6))
    except ValueError:
      print('Are you sure that you dataframe has non-object columns?')
    except NameError:
      print('Are you sure that you have not skiped read_json?')

  def save_plots(self):
    import matplotlib.pyplot as plt
    import os
    if not os.path.exists('results'):
      os.makedirs('results')
    try:
      df = self.read_json(path)
      for column in df.select_dtypes(exclude='object').columns:
        plt.title(column)
        df[column].hist(figsize=(4,4))
        plt.savefig(f'results/{column}.png')
        plt.clf()
      print('Saving completed!')
    except NameError:
      print('Are you sure that you have not skiped previous steps?') 

  def return_paths(self):
    import os
    try:
      for file in os.listdir('results'):
        file_path = os.path.join('results', file)
        print(file_path)
    except NameError:
        print('Are you sure that you have not skiped previous steps?')

  def draw_plots(self, path):
      import pandas as pd
      import matplotlib.pyplot as plt
      import os
      df = self.read_json(path)
      if not os.path.exists('results'):
        os.makedirs('results')
      for column in df.select_dtypes(exclude='object').columns:
        plt.title(column)
        df[column].hist(figsize=(4,4))
        plt.savefig(f'results/{column}.png')
        plt.clf()
      df.hist(layout=(-1, 6), figsize=(16,6))
      for file in os.listdir('results'):
        file_path = os.path.join('results', file)
        print(file_path)
      breakpoint()


string = """docusketch_test().draw_plots('https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json')"""
eval(string)