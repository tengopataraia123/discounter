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