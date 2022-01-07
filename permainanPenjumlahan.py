import tkinter as tk
from tkinter import ttk, messagebox
from random import randint
import sys

class Demo():
	def __init__(self):
		self.root = tk.Tk()
		self.root.geometry("675x700")
		self.root.configure(bg='light blue') 
		
	
		self.root.title("P E R M A I N A N")
		self.body()
		self.root.mainloop()
		
	def body(self):
		self.judul = tk.Label(self.root,text = " P e n j u m l a h a n",font = ("Times",12,"bold"))
		self.judul.configure(bg='light blue',fg = 'red') 
		self.judul.pack(pady = 35)
		
		self.angka1 = tk.Label(self.root,text = "1",font = ("Times",20,'bold'))
		self.angka1.configure(bg='light blue',fg = 'blue') 
		self.angka1.pack()
		

		
		
		self.operator = tk.Label(self.root,text = "+", font = ("Times",18,"bold"))
		self.operator.configure(bg='light blue',fg = 'green') 
		self.operator.pack(side = tk.TOP)
		
		self.angka2 = tk.Label(self.root,text = "4",font = ("Times",20,'bold'))
		self.angka2.configure(bg='light blue',fg = 'blue') 
		self.angka2.pack()
		
		self.jawab = tk.Entry(self.root, justify = tk.CENTER,font = ("Times",10,"bold"))
		self.jawab.pack(pady = 25)
		
		self.add = tk.Button(self.root, text = "Submit", width = 10,command = self.hitung)
		self.add.configure(bg='light blue',fg = 'red') 
		self.add.pack(pady = 20)
		
		self.exit = tk.Button(self.root, text = "Exit", width = 8, command = self.exit)
		self.exit.configure(bg = 'red', fg = 'light blue')
		self.exit.pack()
		
	def hitung(self):
		
		randomAngka = randint(1,100)
	
				
		
		
		try:
			jawaban = int(self.jawab.get())
				
			angkaPertama = int(self.angka1['text'])
				
			angkaKedua = int(self.angka2['text'])
			
			hasil = angkaPertama + angkaKedua
			
			if hasil  ==  jawaban:
				messagebox.showinfo("Benar ", "Selamat ! Anda Benar ")
			else:
				messagebox.showinfo("Salah  ", "Anda Salah")
				
		except:
				pass
				
		self.angka1.config(text = str(randomAngka))
			
					
		self.angka2.config(text = str(randomAngka))
		
		self.jawab.delete(0, "end")
	
	def exit(self):
			sys.exit(0)
				
	
			
			

if __name__ == "__main__":
	app = Demo()
