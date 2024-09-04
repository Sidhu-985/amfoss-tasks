document.addEventListener('DOMContentLoaded', function() {
    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    const total = parseFloat(localStorage.getItem('total')) || 0;

    const cartItemsDiv = document.getElementById('cart-items');
    if (cart.length > 0) {
        cartItemsDiv.innerHTML += `<h2>Your Shopping Cart</h2>
        <p>ID: ${Math.random()*10000000000000000}</p>`;

        cart.forEach(product => {
            cartItemsDiv.innerHTML += `
                <div class="cart-item">
                    <h3>${product.title}</h3>
                    <img src="${product.image}" class="product-image" alt="${product.title}" title="${product.title}">
                    <p style="background-color:green;color:white;border:none;border-radius:30px;padding:10px;">Price: $${product.price.toFixed(2)}</p>
                </div>
            `;
        });
    } else {
        cartItemsDiv.innerHTML = '<p>Your cart is empty.</p>';
    }

    const totalPriceDiv = document.getElementById('total-price');
    totalPriceDiv.innerHTML += `<p style="font-size:25px;">Shipping <strong style="float:right">FREE</strong></p>
    <p style="font-size:25px;">Total TAX <b style="float:right">$52.48</b></p>
    <h2>Total Amount <b style="float:right">$${total.toFixed(2)}</b></h2>
    <a href="">Got a gift card or a promotional code</a>`;

    document.getElementById('complete-purchase').addEventListener('click', function() {
        localStorage.removeItem('cart');
        localStorage.removeItem('total');
        alert('Thank you for your purchase!');
        window.location.href = 'index.html'; 
    });
});
