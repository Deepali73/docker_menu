import os

while True:
    print(
        """
        ---------------------------------------------------------
                 DOCKER MENU BASED PROGRAM
        ---------------------------------------------------------
        1. Launch new container
        2. Stop the container
        3. Remove the container
        4. Start the container 
        5. List all the containers
        6. List all the images
        7. Pull image from Docker Hub
        8. Remove a specific image
        9. Remove all Docker images
        10. Exit  
        """
    )
    
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter the name of container: ")
        image = input("Enter the name of image: ")
        os.system(f"docker run -dit --name {name} {image}")

    elif choice == "2":
        name = input("Enter the name of container: ")
        os.system(f"docker stop {name}")

    elif choice == "3":
        name = input("Enter the name of container: ")
        os.system(f"docker rm -f {name}")

    elif choice == "4":
        name = input("Enter the name of container: ")
        os.system(f"docker start {name}")

    elif choice == "5":
        os.system("docker ps -a")

    elif choice == "6":
        os.system("docker images")

    elif choice == "7":
        image = input("Enter the image name to pull (e.g., nginx:latest): ")
        os.system(f"docker pull {image}")

    elif choice == "8":
        image = input("Enter the name of image to remove: ")
        os.system(f"docker rmi {image}")

    elif choice == "9":
        confirm = input("Are you sure you want to remove ALL images? (yes/no): ")
        if confirm.lower() == "yes":
            os.system("docker rmi $(docker images -q)")

    elif choice == "10":
        print("Exiting... 🚪")
        break

    else:
        print("⚠️ Please enter a valid option (1-10)!")
