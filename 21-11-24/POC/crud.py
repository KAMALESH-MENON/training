from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Step 1: Define the Database URL (SQLite for simplicity)
DATABASE_URL = "sqlite:///./products.db"

# Step 2: Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Step 3: Create the Base class for the models
Base = declarative_base()

# Step 4: Define the Product model (table)
class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    quantity_in_stock = Column(Integer)

    def __repr__(self):
        return f"Product(id={self.id}, name={self.name}, quantity_in_stock={self.quantity_in_stock})"


# Step 5: Create the session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Step 6: Create the tables in the database
Base.metadata.create_all(bind=engine)

# Step 7: CRUD Operations
def create_product(db_session, name: str, description: str, quantity_in_stock: int):
    db_product = Product(name=name, description=description, quantity_in_stock=quantity_in_stock)
    db_session.add(db_product)
    db_session.commit()
    db_session.refresh(db_product)
    return db_product

def get_all_products(db_session):
    return db_session.query(Product).all()

def get_product_by_id(db_session, product_id: int):
    return db_session.query(Product).filter(Product.id == product_id).first()

def update_product(db_session, product_id: int, name: str, description: str, quantity_in_stock: int):
    db_product = db_session.query(Product).filter(Product.id == product_id).first()
    if db_product:
        db_product.name = name
        db_product.description = description
        db_product.quantity_in_stock = quantity_in_stock
        db_session.commit()
        db_session.refresh(db_product)
        return db_product
    return None

def delete_product(db_session, product_id: int):
    db_product = db_session.query(Product).filter(Product.id == product_id).first()
    if db_product:
        db_session.delete(db_product)
        db_session.commit()
        return db_product
    return None

# Step 8: Example Usage
if __name__ == "__main__":
    # Step 8.1: Create a session
    session = SessionLocal()

    # Step 8.2: Create products
    print("Creating products...")
    product1 = create_product(session, "Widget A", "A small widget", 100)
    product2 = create_product(session, "Widget B", "A large widget", 200)
    print(f"Created products: {product1}, {product2}")

    # Step 8.3: Retrieve all products
    print("\nAll Products:")
    products = get_all_products(session)
    for product in products:
        print(product)

    # Step 8.4: Retrieve a product by ID
    print("\nRetrieving product with ID 1:")
    product = get_product_by_id(session, 1)
    print(product)

    # Step 8.5: Update a product
    print("\nUpdating product with ID 1...")
    updated_product = update_product(session, 1, "Widget A Updated", "An updated small widget", 150)
    print(updated_product)

    # Step 8.6: Delete a product
    print("\nDeleting product with ID 2...")
    deleted_product = delete_product(session, 2)
    print(f"Deleted: {deleted_product}")

    # Step 8.7: Retrieve all products after deletion
    print("\nAll Products After Deletion:")
    products = get_all_products(session)
    for product in products:
        print(product)

    # Step 8.8: Close the session
    session.close()