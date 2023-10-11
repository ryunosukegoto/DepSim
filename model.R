pkgLoad <- function( packages = "favourites" ) {
    if( length( packages ) == 1L && packages == "favourites" ) {
        packages <- c( "data.table", "chron", "plyr", "dplyr", "shiny",
                       "shinyjs", "parallel", "devtools", "doMC", "utils",
                       "stats", "microbenchmark", "ggplot2", "readxl",
                       "feather", "googlesheets", "readr", "DT", "knitr",
                       "rmarkdown", "Rcpp"
        )
    }
    
    packagecheck <- match( packages, utils::installed.packages()[,1] )
    
    packagestoinstall <- packages[ is.na( packagecheck ) ]
    
    if( length( packagestoinstall ) > 0L ) {
        utils::install.packages( packagestoinstall,
                                 repos = "http://cran.csiro.au"
        )
    } else {
        print( "All requested packages already installed" )
    }
    
    for( package in packages ) {
        suppressPackageStartupMessages(
            library( package, character.only = TRUE, quietly = TRUE )
        )
    }
}

pkgLoad(list("randomForest","caret","grf","dplyr"))

library(randomForest)
library(caret)
library(grf)
library(dplyr)

load("cfmodel.RData")

causalForest <- function(data){
    df = t(data.frame(data))
    predictions = predict(cf.dep.scr, df)
    return(predictions$predictions)
}