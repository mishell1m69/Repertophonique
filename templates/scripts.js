function afficherPopup(event) {
    event.preventDefault(); // empêche le lien de fonctionner normalement
    var popup = confirm("Voulez-vous continuer ?");
    if (popup) {
      // si l'utilisateur appuie sur "OK", on continue normalement
      window.location.href = event.target.href;
    }
  }
  
  // sélectionne le lien
  var lienSpecifique = document.getElementById("liengithub");
  
  lienSpecifique.addEventListener("click", afficherPopup);