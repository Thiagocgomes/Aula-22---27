import tkinter as tk
import requests


def get_lyrics():
  artist = artista_entry.get()
  song = song_entry.get()

  api_url = f'https://api.vagalume.com.br/search.php?art={artist}&mus={song}'
  response = requests.get(api_url)

  if response.status_code == 200:
    data = response.json()
    lyrics = data['mus'][0]['text']
    display_lyrics(lyrics)
  else:
    result_label.config(text = 'Não encontrado')

def display_lyrics(lyrics):
  result_text.delete(1.0, 'end')
  result_text.insert(tk.END, lyrics)

root = tk.Tk()
root.title('Busque sua musica ;)')
root.geometry('400x400')

artista_label = tk.Label(root, text = 'Digite o artista')
artista_label.pack()
artista_entry = tk.Entry(root)
artista_entry.pack()

song_label = tk.Label(root, text ='Digite a musica')
song_label.pack()
song_entry = tk.Entry(root)
song_entry.pack()

btn = tk.Button(root, text = 'Buscar', command = get_lyrics)
btn.pack()

result_text = tk.Text(root)
result_text.pack()

result_label = tk.Label(root, text= '')
result_label.pack()


root.mainloop()