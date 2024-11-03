var currentSlide = 0;
var slides = document.querySelectorAll('.slide');
var totalSlides = slides.length;

// Slider'ın manuel kaydırma işlevi (önceki ve sonraki)
function showSlide(index) {
  if (index >= totalSlides) {
    currentSlide = 0;
  } else if (index < 0) {
    currentSlide = totalSlides - 1;
  } else {
    currentSlide = index;
  }

  // Slider'ın kaydırılması
  var newTransformValue = -currentSlide * 598;
  document.querySelector('.slides').style.transform = `translateX(${newTransformValue}vh)`;
}

// Önceki slayta geçme
function prevSlide() {
  showSlide(currentSlide - 1);
}

// Sonraki slayta geçme
function nextSlide() {
  showSlide(currentSlide + 1);
}

// Otomatik kaydırma işlevi
function autoSlide() {
  nextSlide();
}

// Her 3 saniyede bir otomatik slayt kaydırma
var slideInterval = setInterval(autoSlide, 3000);

// Fare üzerine gelince otomatik kaydırmayı durdurma
document.querySelector('.slider').addEventListener('mouseover', () => {
  clearInterval(slideInterval);
});

// Fare çekildiğinde otomatik kaydırmaya devam etme
document.querySelector('.slider').addEventListener('mouseout', () => {
  slideInterval = setInterval(autoSlide, 5000);
});