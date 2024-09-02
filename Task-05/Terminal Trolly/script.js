const terminalOutput = document.querySelector('.terminal-output');
const terminalInput = document.querySelector('input[type="text"]');
const productCatalog = document.querySelector('.product-catalog');
let products = [];
const cart = [];

terminalInput.addEventListener('keydown', function (event) {
    if (event.key === 'Enter') {
        handleInput(terminalInput.value.trim());
    }
});

async function fetchProducts() {
    try {
        const response = await fetch('https://fakestoreapi.com/products');
        if (response.status!=200) {
            throw new Error('Network response was not ok');
        }
        products = await response.json();
        displayProducts(products);
    } catch (error) {
        terminalOutput.textContent += 'Error fetching products\n';
    }
}

function displayProducts(products) {
    productCatalog.innerHTML = '';
    products.forEach(product => {
        const productDiv = document.createElement('div');
        productDiv.classList.add('product');
        productDiv.innerHTML = `
            <h3>${product.title}</h3>
            <p>Price: $${product.price}</p>
            <img src="${product.image}" alt="${product.title}" style="max-width: 100px; height: auto;" title="${product.title}">
        `;
        productCatalog.appendChild(productDiv);
    });
}

function handleInput(command) {
    
    clearTerminal();
    
    const [action, ...args] = command.split(' ');

    switch (action) {
        case 'help':
            help();
            break;
        case 'list':
            listProducts();
            break;
        case 'details':
            viewProductDetails(args[0]);
            break;
        case 'add':
            addToCart(args[0]);
            break;
        case 'remove':
            removeFromCart(args[0]);
            break;
        case 'cart':
            viewCart();
            break;
        case 'buy':
            proceedToCheckout();
            break;
        case 'clear':
            clearTerminal();
            break;
        case 'search':
            searchProduct(args.join(' '));
            break;
        case 'sort':
            sortProducts(args[0]);
            break;
        default:
            terminalOutput.textContent += `Invalid command: ${command}\n`;
            break;
    }

    terminalInput.value = '';
}

function help() {
    terminalOutput.innerHTML += "Available Commands: \n- list: List all products \n- details 'product_id': View product details\n- add 'product_id': Add a product to cart\n- remove 'product_id': Remove a product from cart\n- cart: View your cart\n- buy: Buy all products in the cart\n- search [query]: Search products by name\n- sort [price/name]: Sort products by price or name\n- clear: Clear the screen\n";
}

function listProducts() {
    if (products.length === 0) {
        terminalOutput.innerHTML += 'No products available.\n';
        return;
    }

    terminalOutput.innerHTML += 'Listing all products...\n';
    products.forEach(product => {
        terminalOutput.innerHTML += `${product.id} - ${product.title} - $${product.price}\n`;
    });
}

function viewProductDetails(productId) {
    const product = products.find(p => p.id === parseInt(productId));
    if (product) {
        terminalOutput.innerHTML += `ID: ${product.id}\nTitle: ${product.title}\nDescription: ${product.description}\nPrice: $${product.price}\n`;
    } else {
        terminalOutput.innerHTML += `Product with ID ${productId} not found.\n`;
    }
}

function addToCart(productId) {
    const product = products.find(p => p.id === parseInt(productId));
    if (product) {
        if (!cart.some(p => p.id === product.id)) {
            cart.push(product);
            terminalOutput.innerHTML += `Added ${product.title} to cart.\n`;
        } else {
            terminalOutput.innerHTML += `${product.title} is already in the cart.\n`;
        }
    } else {
        terminalOutput.innerHTML += `Product with ID ${productId} not found.\n`;
    }
}

function removeFromCart(productId) {
    const index = cart.findIndex(p => p.id === parseInt(productId));
    if (index !== -1) {
        const removedProduct = cart.splice(index, 1)[0];
        terminalOutput.innerHTML += `Removed ${removedProduct.title} from cart.\n`;
    } else {
        terminalOutput.innerHTML += `Product with ID ${productId} not in cart.\n`;
    }
}

function viewCart() {
    if (cart.length > 0) {
        terminalOutput.innerHTML += 'Items in your cart:\n';
        cart.forEach(product => {
            terminalOutput.innerHTML += `ID: ${product.id} - ${product.title} - $${product.price}\n`;
        });
    } else {
        terminalOutput.innerHTML += 'Your cart is empty.\n';
    }
}

function proceedToCheckout() {
    if (cart.length > 0) {
        const total = cart.reduce((sum, product) => sum + product.price, 0);

        localStorage.setItem('cart', JSON.stringify(cart));
        localStorage.setItem('total', total);

        window.location.href = 'checkout.html';
    } else {
        terminalOutput.innerHTML += 'Your cart is empty. Add items to your cart before proceeding to checkout.\n';
    }
}

function clearTerminal() {
    terminalOutput.innerHTML = '';
}

function searchProduct(productName) {
    const results = products.filter(p => p.title.toLowerCase().includes(productName.toLowerCase()));
    if (results.length > 0) {
        results.forEach(product => {
            terminalOutput.innerHTML += `ID: ${product.id} - ${product.title} - $${product.price}\n`;
        });
    } else {
        terminalOutput.innerHTML += `No products found for search: ${productName}\n`;
    }
}

function sortProducts(criteria) {
    if (criteria === 'price') {
        products.sort((a, b) => a.price - b.price);
    } else if (criteria === 'name') {
        products.sort((a, b) => a.title.localeCompare(b.title));
    } else {
        terminalOutput.innerHTML += `Unknown sorting criteria: ${criteria}\n
        Please enter in this format\n sort name or price`;
        return;
    }
    terminalOutput.innerHTML += `Products sorted by ${criteria}\n`;
    displayProducts(products); 
}

fetchProducts();
