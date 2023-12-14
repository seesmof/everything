class Shopkeeper:
    def __init__(self, products):
        self.products = products
        self.popularProducts = []
        self.productsFreqency = {product: 0 for product in products}

    def solveProblem(self, customerOrder):
        queueTime = 0
        print(f"Popular products: {self.popularProducts}")
        for order in customerOrder:
            originalQueueTime = queueTime
            if order in self.popularProducts:
                queueTime += 1
            elif order in self.products:
                queueTime += 2
                self.productsFreqency[order] += 1
            else:
                queueTime += 3
            print(f"Queue time: +{queueTime - originalQueueTime} for {order}")
        self.updatePopularProducts()
        return queueTime

    def updatePopularProducts(self):
        mostPopularProduct = max(self.productsFreqency, key=self.productsFreqency.get)
        self.popularProducts.append(mostPopularProduct)
        del self.productsFreqency[mostPopularProduct]


products = [
    "cheese",
    "milk",
    "bread",
    "butter",
    "eggs",
    "flour",
    "sugar",
    "salt",
    "potatoes",
    "tomatoes",
]
shopObject = Shopkeeper(products)
orders = [
    "cheese,milk,yogurt",
    "bread,butter,cheese",
    "eggs,cheese,flour",
    "bread,eggs,milk",
    "bread,cheese,flour",
    "pepper,cheese,milk",
]

for order in orders:
    orderItems = order.split(",")
    print(f"For {order} the queue time is {shopObject.solveProblem(orderItems)}\n")
