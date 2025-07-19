livres = [
    {"titre": "python débutant", "auteur": "Dupont", "année": 2008},
    {"titre": "Maîtriser python", "auteur": "Durand B", "année": 2015},
    {"titre": "python avancé", "auteur": "Martin", "année": 2021},
]

print("Livres publiés après 2010 :")
for livre in livres:
    if livre["année"] > 2010:
        print(f"{livre['titre']} ({livre['année']})-{livre['auteur']}")
