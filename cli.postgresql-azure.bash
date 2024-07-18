namerg=postgresqlrg
location=eastus
servername=s1620mdatabi
adminpassword=S16-20-m-data-bi
dbname=hidropt

# crear un grupo de recursos
az group create --name $namerg --location $location

#crear un postgres server
az postgres server create --name $servername \
                            --resource-group $namerg \
                            --location $location \
                            --admin-user fidel \
                            --admin-password $adminpassword \
                            --sku-name B_Gen5_1

#crear db en server
az postgres db create --name $dbname \
                        --resource-group $namerg \
                        --server-name $servername