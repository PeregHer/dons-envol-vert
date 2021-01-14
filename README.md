# Page de promesse de don - Envol Vert

## Présentation des pages
- Une page d'accueil nommée `index.html`
- Une page pour effectuer des dons nommée `don.html`
- Une page pour visualiser les derniers donateurs nommée `donateurs.html`
- Une page pour lire des conditions générales nommée `conditions.html`
- Une page pour se connecter au panel admin nommée `login.html`
- Une page admin pour visualiser les dons nommée `admin.html`

## Présentation de la base de données

La base de données a été créée sur MongoDB Atlas. Il y a une seule collection nommée `dons` située dans la base de donnée nommée `flask`

Chaque objet dans la collection est crée comme ceci:

`{nom: 'Nom', prenom: 'Prenom', email: 'prenom.nom@gmail.com', telephone: '0678526023', date: '2021/01/14', montant: 100}`
