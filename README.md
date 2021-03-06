# Getting PostgreSQL Running With Google Cloud

## Deploying a VM

Navigate to cloud.google.com and create a project (or select our existing
project, if re-implementing a VM).

Select Compute Engine, from the navigation menu, and then select VM instances.
Create New Instance, and choose create.  (If you are doing this from scratch.)

Set the name to something meaningful, like:
```
  postgres-server-1
```

Set the region to:
```
  us-west1 (Oregon).
```

Under Machine configuration, in the general-purpose tab select Series N1
from the first dropdown menu, and Machine type g1-small from the second
dropdown menu.

In the Boot Disk section, click on Change to configure the boot disk.
Select Ubuntu 18.04 LTS from the preconfigured image tab.  Boot disk type
should be set to Standard Persistent Disk, and click Select.

In the firewall section, check the boxes for
```
  'Allow HTTP traffic'
```
And
```
  'Allow HTTPS traffic'
```

Click on Create to finalize the VM.

On the VM instances page, click on the instance, and then click on the SSH
button.


##Updating the VM and Installing PostgreSQL

Update the packages for the server using the command:
```
  sudo apt-get update
```

Install PostgreSQL using the command:

```
  sudo apt-get -y install postgresql postgresql-client postgresql-contrib
```

Run the shell in SSH with the command:
```
  sudo -s
```

Run PSQL as the default user (which is conveniently called postgres):
```
  sudo -u postgres psql postgres
```

You should see the default PSQL command prompt, postgres=#
Set a password using the command
```
  \\password postgres
```

Then confirm the password.
Install the adminpack extension to enable server instrumentation.  The console
will return CREATE EXTENSION if it succeeds.
```
  CREATE EXTENSION adminpack;
```

Exit PSQL, then exit the root shell.
Enable remote connections by editing the pg_hba.conf file.  Access this with
```
  sudo vim ../../etc/postgresql/10/main/pg_hba.conf
```

Determine the IP address of your local computer.  At the bottom of the file,
add the following lines, replacing [YOUR_IPV4_ADDRESS] with your actual IPv4
address:
```
#IPv4 remote connections:
host    all             all           [YOUR_IPV4_ADDRESS]/32         md5
```

Save and exit vim, then open postgresql.conf with:
```
  sudo vim ../../etc/postgresql/10/main/postgresql.conf
```

Locate the line which begins with #listen_addresses = 'localhost', then delete
the #, and replace 'localhost' *.  It should read:
```
  listen_addresses = '\*'
```

Postgres will now listen across all IP addresses.  Save the file and exit, then
restart the database service using:
```
  sudo service postgresql restart
```

We need to set up a firewall rule in order to allow access to this database.
This can be set up in a number of different ways - we will set it up in the
*least* secure way possible for now (Aidan, you may need to alter this for
Full Stack in order to limit direct access to the PostgreSQL server - but for
now this is a viable setting because nothing is publicizing the location of
this server in any way, and because we are all going to eventually have to add
the variety of IPv4 addresses from which we may need to remotely access this
server to the pg_hba.conf file, as listed above).

Leave Network field as default; name the new firewall rule something like
```
postgres-analytics-ingress).
```
In the direction of traffic, select:
```
  ingress
```

In the Targets dropdown menu, select:
  all instances in the network

In source IP ranges, enter:
```
  0.0.0.0/32.
```

In Allowed protocols and ports, check the box for TCP:
```
  5432
```

Then click create. Now repeat all of these steps, selecting egress instead of ingress.

## Setting up a static IP address

From the VPC network dropdown menu, select External IP addresses.  You should
see a listing of the External addresses for every VM you have created, and
which is still active in the project.  Type will be listed as 'Ephemeral'.
Click the arrow next to Ephemeral to bring up a dropdown menu; then select
static.  You will be prompted to name the new static IP address, provide an
optional description, and then click 'Reserve'.  This will ensure that we
have a static IP address for this VM, which doesn't change every time we
need to stop and start the VM or reboot it.  It may take a few minutes to
activate.

NOTE: For greater security, we can turn this rule off and use the exact IPv4
address that we added to the pg_hba.conf file... with the caveat that you will
have to make a new rule AND add every new address to pg_hba.conf whenever you
need to log in from a different location or a non-static IP address.

##Connecting to PostgreSQL

Now we can connect to Postgres.  Install pgAdmin (or a similar Postgres client)
on your computer.

You'll need to add the server to your client.  You'll typically have to name
the server, and definitely have to provide the IP address for the server.  To
find the server's IP address, head back to the VM instances page on the Cloud
Dashboard, and locate the IP address of the VM running Postgres.

In the Host field in your client, enter the external IP address of your Compute
Engine instance.  In the port field, specify port 5432

In the password field, enter the password you set up for the default user
(postgres).

You should now be able to access Postgres.

## Creating a snapshot for easy backup

When all this setup is complete and verified, take a snapshot of the Google
Cloud VM. In the compute engine dropdown menu, select 'Snapshots', then click
the 'Create Snapshot' button.  Give it a name, a description of the checkpoint
you are snapshotting, and select the VM you want to snapshot in the 'Source
Disk' dropdown solution and select multi-regional or regional.  (For our
purposes, and economy of free Google credit, I advise regional.  In a real-life
environment selecting multi-regional would give us a more secure system; if
Google has a catastrophic failure at their Dalles, OR data center, we might
lose both our VM and our VM snapshot if we save both in the same region!
For similar reasons we probably want to pick different zones in the same)

You can add a label, which is just a key:value pair.  This allows you to
group associated resources in larger projects very easily. Is it necessary
for this project? Well... probably not. We'll likely have at most two/three
disks for this.

Click on Create, and you'll have a snapshot ready to go.

### Recovering from our snapshot

If we suffer a catastrophic failure, we can restore from the snapshots, by
creating a new VM using the instructions above.  We name it and change its
location as normal, and select a machine configuration which matches our
original set of parameters.  When we get to the 'Boot Disk' section, click
on change, and then select the snapshots tab.  This tab should have a listing
for the snapshot we just created.

### Loading Data

The WB-DataGenerator.py program in this repo will generate a number of tuples
as specified at the command line by the user.  A number of different functions
are run within the framework of that request, each of which creates the dataset
for a single attribute of the scalable Wisconsin Benchmark database schema, as
detailed on page 8 of Dewitt's paper, _Wisconsin Benchmark: Past, Present and
Future_.  After the data is created, it will be written to a CSV file, which
will have to be copied to the server. (We could also run the script over there,
of course).  To copy it to the server, SSH into the server, and while in your
home directory, click on the settings button in the SSH window.  Select 'Upload
file' and upload it.  You can futz around with PuTTy forever trying to get things
uploaded if you would prefer.  This is just easier.

The create_wb_schema.sql file contains the SQL commands to sequentially
drop the 'wisconsinbenchmark' database if it already exists, then create the
'wisconsinbenchmark' database with ownership by the postgres superuser, \connect
to that database, create a table with the appropriate schema (again, as detailed
on DeWitt), alter that table so that its owner is also the default user, and
finally copy the CSV file into the schema.  This can all be run from within
PostgreSQL by using the command:
```
\i create_wb_schema.sql
```
Or from the command line, using the following pair of commands:
```
sudo su postgres
psql -f create_wb_schema.sql
```
Note that the create_wb_schema.sql script is hard coded to look for the data at
'/home/wamass/benchmark_data.csv' so make sure to alter the script to reflect
your /home/ directory on the Postgres server prior to attempting to run the script
(although it will run from Will's directory - a copy of the data will be there in
perpetuity.)

The current benchmark_data.csv file consists of 100000 tuples, numbered from 0 to
99999 in unique2 (which serves as the primary key for the table).  This produces
a table roughly five times the size of the default memory buffer (4096 Kb) deployed
in PostgreSQL.  Some fine tuning may be required to determine if this number of
tuples should be dialed down to about 80000 for better benchmarking purposes.  It
was simply chosen as being a factor of 10 higher than the Scalable 'TENKTUP' table
referenced in DeWitt.

##### ReadMe version 1.2
##### William Mass
##### Last Updated - 2/3/20
