

const burgerButton = () => {
  const button = document.querySelectorAll(".toggle")
  if (button[0].classList.contains("is-active")) {
    button[0].classList.remove("is-active");
    button[1].classList.remove("is-active");
  }
  else {
    button[0].classList.add("is-active")
    button[1].classList.add("is-active")
  }
}