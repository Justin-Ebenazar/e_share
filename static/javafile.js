function flipme(){
    const palagai=document.getElementById('flipper');
    palagai.classList.toggle('flipped');
    console.log(123);
}

num_of_files=0;

document.addEventListener('DOMContentLoaded', () => {
    const btn = document.getElementById('add-images-btn');
    const input = document.getElementById('image-input');
    const imagesDiv = document.getElementById('selected-images');
    imagesDiv.style.display='flex';
  
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      input.click();
  });

  
    input.addEventListener('change', (e) => {
      const scr=document.getElementById('scroll-button');
      const files = e.target.files;
      console.log(123)
  
      for (const file of files) {
        const imageContainer = document.createElement('div');
        imageContainer.className = 'image-container';
        imageContainer.style.display='flex';
        imageContainer.style.flexDirection='column';
        imageContainer.style.color='black';
        imageContainer.style.alignItems='flex-end';

        const contain_img=document.createElement('div');
        contain_img.className='img-contain'

        const image = document.createElement('img');
        image.src = URL.createObjectURL(file);

        image.style.backgroundColor='black';
        image.style.setProperty('width', '100%'); 
        image.style.setProperty('height', '100%'); 
        image.style.setProperty('object-fit', 'contain'); 
        
        const deleteBtn = document.createElement('button');
        deleteBtn.textContent = 'x';
        deleteBtn.className = 'delete-btn';

        imageContainer.appendChild(deleteBtn);
        contain_img.appendChild(image)
        imageContainer.appendChild(contain_img);
        imagesDiv.appendChild(imageContainer);
        num_of_files+=1;
  
        deleteBtn.addEventListener('click', () => {
          imageContainer.remove();
          num_of_files-=1;
        });
      }
    });
  });

const scrollableDiv = document.getElementById('selected-images');
var scrollwidth =  window.innerHeight*0.4 ;
var scrollcount=1;


function scrollxf() {
  if (scrollcount != num_of_files) {
    scrollableDiv.scrollLeft += window.innerHeight * 0.4;
    scrollcount += 1;
  }
}

function scrollxb() {
  if (scrollcount != 0) {
    scrollableDiv.scrollLeft -= window.innerHeight * 0.4;
    scrollcount -= 1;
  }
}
  
function virka_close(){
  const virka=document.getElementById('new_product_sale');
  virka.style.display='none';
}

function virka_open(){
  const virka=document.getElementById('new_product_sale');
  virka.style.display='flex';
}
