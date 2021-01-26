TP3 réalisé par Inas BEKKOUCHE et Azzedine AIT ALI BELKACEM .

L'objectif de ce TP est de réaliser une classe de Bike Station (La station VLille) pour pouvoir y accéder à toutes informations de cette station , son nom , sa capacité , combien de vélos elle a et le prix du jour.

1_ Generate and consult javadoc
-------------------------------

We generate the javadoc using the command:

       bash$ javadoc Bike.java BikeStation.java -d docs

Example :
ubuntu@ubuntu-Inspiron-15-3567:~/Bureau/S4/POO/aitalibelkacem_bekkouche_poo/TP03/fichiers-tp3-bike/TP3$ javadoc Bike.java BikeStation.java -d docs
Loading source file Bike.java...
Loading source file BikeStation.java...
Constructing Javadoc information...
Standard Doclet version 11.0.6
Building tree for all the packages and classes...
Generating docs/Bike.html...
Generating docs/BikeStation.html...
Generating docs/package-summary.html...
Generating docs/package-tree.html...
Generating docs/constant-values.html...
Building index for all the packages and classes...
Generating docs/overview-tree.html...
Generating docs/index-all.html...
Building index for all classes...
Generating docs/allclasses-index.html...
Generating docs/allpackages-index.html...
Generating docs/deprecated-list.html...
Building index for all classes...
Generating docs/allclasses.html...
Generating docs/allclasses.html...
Generating docs/index.html...
Generating docs/help-doc.html...

3_ Compile and execute the tests
--------------------------------
Before executing the tests you have to compile the necessary files.

BikeStationTest for example
To compile use the command:

      bash$ javac -classpath test-1.7.jar test/BikeStationTest.java

To execute the tests use the command:

      bash$ java -jar test-1.7.jar BikeStationTest

4_ Execute the programs
------------------------
************************
BikeMain file for example
ubuntu@ubuntu-Inspiron-15-3567:~/Bureau/S4/POO/aitalibelkacem_bekkouche_poo/TP03/fichiers-tp3-bike/TP3$ java BikeMain
false
bike id: b001, model : CLASSICAL et son prix :10



BikeStationMain file :
ubuntu@ubuntu-Inspiron-15-3567:~/Bureau/S4/POO/aitalibelkacem_bekkouche_poo/TP03/fichiers-tp3-bike/TP3$ java BikeStationMain 1 2 3

 The ID of the bike taken at position 0 is: b001, Its rantal price is : 10 euros

 The ID of the bike taken at position 1 is: b002, Its rantal price is : 10 euros

 Sorry, there is no available bike at the position 3