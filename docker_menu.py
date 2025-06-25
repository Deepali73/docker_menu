import os
while True:
  print(
	        """
		---------------------------------------------------------
		         DOCKER MENU BASED PROGRAM
		---------------------------------------------------------
		1.Launch new container
		2.Stop the container
		3.Remove the container
		4.Start the container 
		5.List all the containers
		6.List all the images
		7.Pull image from docker hub
		8.Remove the image
		9.Remove all the images
		10.Exit  
                """
                )
  choice = input("Enter your choice: ")
  if choice=="1":
         	name = input("Enter the name of container:")
         	image = input("Enter the name of image:")
         	os.system(f"docker run -dit --name={name} {image}")
  elif choice=="2":
         	name = input("Enter the name of container:")
         	os.system(f"docker stop {name}")
  elif choice=="3":
         	name = input("Enter the name of container:")
         	os.system(f"docker rm -f {name}")
  elif choice=="4":
         	name = input("Enter the name of container:")
         	os.system(f"docker rm start {name}")
  elif choice=="5":
         	os.system(f"docker ps -a")
  elif choice=="6":
         	os.system(f"docker images")
  elif choice=="7":
         	os.system(f"docker pull nginx:latest")
  elif choice=="8":
                image = input("Enter the name of image:")
                os.system(f"docker rmi {image}")
  elif choice=="9":
  		os.system(f"docker rmi images:latest")                     	
  elif choice=="10":
         	break
  else:
         	print("Enter correct option") 							
         			      
