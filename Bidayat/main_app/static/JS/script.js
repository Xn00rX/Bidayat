/// slideshow animaion starts here
window.onload = function () {
  imgs = document.getElementById('slideshow').children
  interval = 4000
  currentPic = 0
  imgs[currentPic].style.webkitAnimation = 'fadey ' + interval + 'ms'
  imgs[currentPic].style.animation = 'fadey ' + interval + 'ms'
  let infiniteLoop = setInterval(function () {
    imgs[currentPic].removeAttribute('style')
    if (currentPic == imgs.length - 1) {
      currentPic = 0
    } else {
      currentPic++
    }
    imgs[currentPic].style.webkitAnimation = 'fadey ' + interval + 'ms'
    imgs[currentPic].style.animation = 'fadey ' + interval + 'ms'
  }, interval)
}

///content ease in animation starts here

function reveal() {
  let reveals = document.querySelectorAll('.reveal')

  for (let i = 0; i < reveals.length; i++) {
    let windowHeight = window.innerHeight
    let elementTop = reveals[i].getBoundingClientRect().top
    let elementVisible = 1

    if (elementTop < windowHeight - elementVisible) {
      reveals[i].classList.add('active')
    } else {
      reveals[i].classList.remove('active')
    }
  }
}

window.addEventListener('scroll', reveal)
