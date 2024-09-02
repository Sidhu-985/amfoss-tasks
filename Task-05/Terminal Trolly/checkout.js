document.addEventListener('DOMContentLoaded', function() {
    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    const total = parseFloat(localStorage.getItem('total')) || 0;

    const cartItemsDiv = document.getElementById('cart-items');
    if (cart.length > 0) {
        cartItemsDiv.innerHTML = '<h2>Your Cart:</h2>';
        cart.forEach(product => {
            cartItemsDiv.innerHTML += `
                <div class="cart-item">
                    <h3>${product.title}</h3>
                    <img src="${product.image}" class="product-image" alt="${product.title}">
                    <p>Price: $${product.price.toFixed(2)}</p>
                </div>
            `;
        });
    } else {
        cartItemsDiv.innerHTML = '<p>Your cart is empty.</p>';
    }

    const totalPriceDiv = document.getElementById('total-price');
    totalPriceDiv.innerHTML = `<h2>Total Price: $${total.toFixed(2)}</h2>`;

    document.getElementById('complete-purchase').addEventListener('click', function() {
        localStorage.removeItem('cart');
        localStorage.removeItem('total');
        alert('Thank you for your purchase!');
        window.location.href = 'index.html'; 
    });
});
