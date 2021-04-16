document.querySelectorAll('.myBtn').forEach(item => {
  item.addEventListener('click', event => {
    parent = item.parentNode
    modal = parent.getElementsByClassName("modal")[0]
    modal.style.display = "block"
    span = modal.getElementsByClassName("close")[0];
    span.addEventListener('click',event=>{
      modal.style.display = "none"
    })
  })
})

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
  if (event.target == modalebay) {
    modalebay.style.display = "none";
  }
  if (event.target == modalvendoo) {
    modalvendoo.style.display = "none";
  }
  if (event.target == modalalibaba) {
    modalalibaba.style.display = "none";
  }
}