# TVshowAPI
<<<<<<< HEAD
Returns popular TV shows and details about them
Python
=======
Returns popular TV shows and details about them. Returns json and also html depending on url in the the request statement.
data is returned from a database hosted on a cassandra kurbenetes cluster of 3 nodes and also from external API https://www.tvmaze.com/api

Cassandra and Kurbenetes
Apache Cassandra is a proven fault-tolerant and scalable decentralized NoSQL database for today’s applications. You can deploy Cassandra on Docker containers or manage Cassandra through Kubernetes.


Getting Started

A google cloud platform account is required at (https://cloud.google.com). 
Python, flask, several libraries shown in imports in the code. docker image . knowledge of Kurbenetes cli

We created a Kurbenetes cluster
of 3 nodes using the Kurbenetes cli in the interactive google shell terminal.

Steps
1  Build our docker image 
2. Create a Cassandra keyspace with replication configuration
3. create a table and add the data in casandra using cqlash cassandra query language.
4. Push it to the image to Google Repository
5. Run it as a service, exposing the deploment to get an external IP address from Google cloud

Verification and testing
Verify with kubectl to confirm services are running
Test external IP with queries using URLS shown below 

Example http://35.246.101.232/tvshow/Flatmates returns tvshow type as shown in below snapshot

Flatmates is comedy show!



>>>>>>> 454c430e79e06bfd9804e57594027861d958af68
