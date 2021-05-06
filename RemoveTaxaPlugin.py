import PyPluMA

class RemoveTaxaPlugin:
   def input(self, filename):
      #self.myfile = filename
      txtfile = open(filename, 'r')
      parameters = dict()
      for line in txtfile:
         contents = line.split('\t')
         parameters[contents[0]] = contents[1].strip()
      filestuff = open(PyPluMA.prefix()+"/"+parameters['csvfile'], 'r')
      firstline = filestuff.readline()
      self.taxa = firstline.strip().split(',')
      self.pattern = parameters['pattern']
      self.my_mat = []
      self.my_mat.append(self.taxa)
      for line in filestuff:
          self.my_mat.append(line.strip().split(','))
   def run(self):
      self.new_mat = []
      for i in range(0, len(self.my_mat)):
          self.new_mat.append([])
          for j in range(0, len(self.my_mat[i])):
              if (not self.pattern in self.taxa[j]):
                 self.new_mat[i].append(self.my_mat[i][j])
   def output(self, filename):
      filestuff2 = open(filename, 'w')
      
      for i in range(0, len(self.new_mat)):
          for j in range(0, len(self.new_mat[i])):
              filestuff2.write(self.new_mat[i][j])
              if (j != len(self.new_mat[i])-1):
                  filestuff2.write(",")
              else:
                  filestuff2.write("\n")


