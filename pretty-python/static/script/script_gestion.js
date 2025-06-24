document.getElementById('add-form').addEventListener('submit', async function(e) {
  e.preventDefault();
  const name = document.getElementById('product-name').value;

  const res = await fetch('/ajouter-produit', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({ name })
  });

  if (res.ok) {
    location.reload();
  } else {
    alert("Erreur : le produit existe déjà.");
  }
});

function supprimerProduit(name) {
  fetch('/supprimer-produit', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({ name })
  }).then(res => {
    if (res.ok) {
      location.reload();
    } else {
      alert("Erreur lors de la suppression.");
    }
  });
}

