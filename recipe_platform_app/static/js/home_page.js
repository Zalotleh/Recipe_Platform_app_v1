
document.querySelector('.navigationbar-toggler').addEventListener('click', () => {
    document.querySelector('.navigationbar-collapse').classList.toggle('showNav');
});

// transition stopper
let resizeTimer;
window.addEventListener('resize', () => {
    document.body.classList.add('resize-trans-stop');
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(() => {
        document.body.classList.remove('resize-trans-stop');
    }, 400);
});

// text change
const icons = ['apple-alt', 'tree', 'burn'];
const subtext = ['It is all about food', 'get inspired', 'Inspire others'];
const largeText = [
    'create, share, follow, learn.',
    'Eating is a necessity but cooking is an art.',
    'food is passion, food is love.'
];

let count = 1;

function textChange(){
    const mainDiv = document.querySelector('.hero-content-change');

    setInterval(() => {
        mainDiv.innerHTML = `
            <div>
                <span>
                    <i class = "fas fa-${icons[count]}"></i>
                </span>
                <h3>
                    <div class = "line"></div>
                    <span>${subtext[count]}</span>
                    <div class = "line"></div>
                </h3>
                <h1 class = "hero-lg-text">
                    ${largeText[count]}
                </h1>
            </div>
        `;
        count++;
        if(count > 2) count = 0;
    }, 4000);
}
textChange();