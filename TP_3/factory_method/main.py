from store import NYPizzaStore, ChicagoPizzaStore

def main():
    ny = NYPizzaStore(); chi = ChicagoPizzaStore()
    #p1 = ny.order_pizza("cheese"); print("Ethan ordered:", p1)
    #p2 = chi.order_pizza("cheese"); print("Joel ordered:", p2)
    
    # New orders
    # From NY
    p3 = ny.order_pizza("veggie"); print("\nEthan ordered:", p3)
    p4 = ny.order_pizza("pepperoni"); print("\nJoel ordered:", p4)
    print("-----")
    # From Chicago
    p5 = chi.order_pizza("veggie"); print("\nEthan ordered:", p5)
    p6 = chi.order_pizza("pepperoni"); print("\nJoel ordered:", p6)
                                             


if __name__ == "__main__":
    main()
