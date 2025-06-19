# Réalisation d'une vidéo 
## Informations officielles 
D'après https://jdp.esiee.fr/videos-jdp-2025/ 

> L’exposition des projets aura lieu le **2025-06-25 jeudi, de 9:30 à 16:00.** 
> 
> Faire une vidéo vous permet : 
> - de participer au Concours vidéo (3 chèques Kadéos de 150 euros à gagner) 
> - d’obtenir une bonification dans le cadre de vos études. 
> 
> **La vidéo lauréate sera diffusée au public lors de la Remise du Prix.**
> 
> **Notation**
> 
> - Bonne communication en images
> - Compréhension du projet
> - Esthétisme
> - Rythme
> 
> 
> **CONTRAINTES TECHNIQUES** 
> 
> - **Nom de la vidéo :** Mettre le nom du projet 
> - **Poids du fichier** : **inférieur à 19 MB dans la mesure du possible** 
> - **Format** : un fichier MP3/MP4 **ou un lien YouTube**
> - **Contenu** : de la phase de préparation à la phase finale du projet 
> - **Musique et images libres de droits** 
> - **Durée** : entre de 1:30 et 2:30  
> - **Envoyez le lien de votre vidéo à** jourdesprojets@esiee.fr 
> - ==**Date de transmission** : au plus tard le **20 juin 2025 midi.== Le jury se réunit le 23 juin 2025.**  
> 
> **Exemples de vidéos :** https://jdp.esiee.fr/concours-videos-2018/ 

## Idées 
Il faudrait qu'elle attire l'œil. 
À la journée des projets, il y aura beaucoup de bruits, donc soit prévoir des sous-titres, soit du texte intégré qui accompagne la vidéo. 
Pourquoi pas plusieurs versions ? 
Trouver des musiques libres d'usage (chercher "royalty free" en ligne). 

### 2025-06-18 
Une vidéo qui explique notre projet simplement, tout en restant divertissant. 

Plusieurs parties. 

- Nos efforts et notre assiduité 
- Les différents prototypes 
- Explication de la partie théorique 
- Vulgarisation de la partie logicielle 
- Photo de nous 
- Moments marrants ? 

À ne pas oublier : 

- Égalisation du son 
- Crédits (musique, images, sons... ) à la fin de la vidéo 
- 

## Comment 
Un logiciel de composition vidéo. 

- Davinci Resolve : avancé et complet 
- Kdenlive : moyennement avancé, simple 
- Premiere Pro : avancé mais... adobe 
- Shotcut : aucune idée 
- Blender : avancé, possible mais peut-être pas évident 

Des outils pour faire des animations. 

- Animations mathématiques : [Manim](https://www.manim.community/) 
- Tout : [Blender](https://www.blender.org/) 
- Polyvalent, 2D : Adobe Animate 

### Media 

Des banques de sons libres d'usage. (Merci [EvilDaystar](https://www.reddit.com/r/Filmmakers/comments/13lwk4l/comment/jkrynys/)) 

- https://soundimage.org/
- https://incompetech.filmmusic.io/search/
- https://www.soundclick.com/artist/default.cfm?bandid=1277008&content=songs
- https://no-copyright-music.com/
- https://uppbeat.io/
- https://sfx.productioncrate.com/royalty-free-music-categories.html
- https://www.scottbuckley.com.au/library/
- https://www.streambeats.com/
- https://www.bensound.com/
- https://www.purple-planet.com/
- https://imuno.sourceaudio.com/#!albums
- https://ncs.io/ 

- https://pixabay.com/sound-effects/ 
- https://pixabay.com/music/ 

Des musiques libres d'usage. 

- Toutes les compositions de Toby Fox. 

D'après https://materiamusicpub.com/youtube-faq/ 

> **Can I use music from games such as UNDERTALE or DELTARUNE in my YouTube videos?**
> 
> You are welcome to include most melodies administered by Materia Music Publishing (including the original recordings from the UNDERTALE® and DELTARUNE® soundtracks) in your videos as long as you’re doing so non-commercially. This means your video is not intended to make you money, it is not sponsored or promoting a product that will make you money, you do not receive ad/subscription/affiliate/marketing/sponsorship revenue for the video, etc. This is determined in Materia’s sole discretion; please reach out should there be concerns about clarity.
> 
> If you use this music non-commercially, YouTube may still receive a claim to let us know that the music is being used. This is not a strike against your channel. There is no penalty or punishment for receiving a claim.
> 
> If you do use music published by Materia Music Publishing, we ask you to please credit the appropriate composer/copyright holder in your video’s description. In the case of UNDERTALE or DELTARUNE, that means crediting Toby Fox as the composer and Materia Music Publishing as the copyright administrator. Giving credit where it’s due is the right thing to do!

Éventuellement : des banques d'images et vidéos libres d'usage. 

- https://pixabay.com/ 

## Utile 
### Télécharger de YouTube 
Pour extraire la vidéo ou l'audio. 

Vidéo. 
```bash
yt-dlp https://youtu.be/xLsuam9o9BA
```

Audio. 
```bash
yt-dlp -x https://youtu.be/xLsuam9o9BA
```

Audio `.wav`. 
```bash
yt-dlp -x --audio-format wav --audio-quality 0 https://youtu.be/xLsuam9o9BA
```

> For video compositing, WAV files are preferred due to their uncompressed quality, which provides the best audio fidelity. M4A and MP3 files are compressed formats that may sacrifice some audio quality for smaller file sizes, making them less ideal for professional audio work.
> 
> [lalal.ai](https://www.lalal.ai/blog/difference-between-audio-formats-mp3-flac-wav-aiff-m4a-ogg/), [caseguard.com](https://caseguard.com/articles/m4a-mp3-and-wav-audio-files-new-technology/) 



