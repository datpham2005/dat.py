import os

FILE_NAME = "products.csv"

# 1. Đọc dữ liệu từ file csv vào danh sách
def read_products():
    products = []
    if not os.path.exists(FILE_NAME):
        return products
        
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        file.readline()  # Bỏ qua dòng tiêu đề (ProductID,ProductName,Price)
        for line in file:
            line = line.strip()
            if not line:
                continue
            data = line.split(",")
            if len(data) >= 3:
                product = {
                    "id": data[0].strip(),
                    "name": data[1].strip(),
                    "price": data[2].strip()
                }
                products.append(product)
    return products

# 2. Hiển thị tất cả sản phẩm
def display_product(products):
    if not products:
        print("\nDanh sách sản phẩm trống!\n")
        return
    print("\n" + "=" * 40)
    print(f"{'ID':<10} | {'ProductName':<18} | {'Price':<10}")
    print("-" * 40)
    for p in products:
        print(f"{p['id']:<10} | {p['name']:<18} | {p['price']:<10}")
    print("=" * 40 + "\n")

# 3. Thêm sản phẩm
# ham them san pham
def add_product(products):
    # cho nhap product id
    product_id = input("Enter Product ID:")
    # kiem tra xem id nay co ton tai hay chua?
    for p in products:
        if p['id'].lower() == product_id.lower():
            print("Id is duplicated")
            return
            
    # nhap tiep name va price khi ID hop le
    product_name = input("Enter Product Name:")
    product_price = input("Enter Product Price:")
    
    # tao dictionary san pham moi va them vao danh sach
    product = {
        "id": product_id,
        "name": product_name,
        "price": product_price
    }
    products.append(product)
    print("Product added successfully!")

# ham tim kiem san pham
def search_product(products):
    search_id = input("Enter Product ID to search:")
    found = False
    for p in products:
        if p['id'].lower() == search_id.lower():
            print(f"ProductID: {p['id']} --- ProductName: {p['name']} --- Price: {p['price']}")
            found = True
            break
    if not found:
        print("Product not found!")

# ham luu vao file
def save_products(products):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        file.write("ProductID,ProductName,Price\n")
        for p in products:
            file.write(f"{p['id']},{p['name']},{p['price']}\n")
    print("Saved products to file successfully!")

# Main Menu
def main():
    # doc du lieu khi chuong trinh chay goi ham read product ()
    products = read_products()

    while True:
        print("********************MENU********************")
        print("1. Display all products")
        print("2. Add products")
        print("3. Search product by id")
        print("4. Save products to file")
        print("5. Exit program")
        print("********************MENU********************")

        choice = input("Enter your choice: ")
        if choice == "1":
            display_product(products)
        elif choice == "2":
            add_product(products)
        elif choice == "3":
            search_product(products)
        elif choice == "4":
            save_file(products)
        elif choice == "5":
            print("Exit Programe")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại!")

if __name__ == "__main__":
    main()