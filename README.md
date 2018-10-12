<div align="center">
        <h1>RescueU</h1>
</div>

Web application that helps intelligently manages calamities and disasters

# Introduction

RescueU is an intelligent disaster prediction and management web
application built on the Django Framework. It provides the following
features for effectively predicting and handling natural calamities

* Instant Rescue Notifications
* Live Location of Victims and Volunteers through Bing Location API
* Intelligent Resource Allocation
* News Headline Analytics for Disaster Prediction
* Data Analytics of Disaster-Prone Areas

## Instant Rescue Notifications

The victims in the disaster-prone areas can, with just a single click on
the SOS button, send an emergency notification to their contacts as well
as all the relief volunteers registered on the site

## Live Location

Using the Bing Location API, the webapp obtains live locations of the
victims and the volunteers. The victims are notified of the volunteers
nearest to them and the volunteers are notified of the victims nearby by a
distress call, which, should they accept, are assigned to that particular
victim or group of victims. Advanced route planning and shortest path
graph algorithms helps the relief volunteers reach the victims through the
shortest possible path. Using the Bing Maps API, the volunteers get an
overview of the general location where the victim is under distress, with
locations of importance such as hospitals and health centers marked.

## Intelligent Resource Allocation

Victims are queried about the resources they require and volunteers are
queried about the resources they possess. Using sophisticated resource
allocation algorithms, volunteers are assigned to disaster prone areas as
per the resources they possess. By applying machine learning and natural
language processing algorithms on live news feed about the disaster-prone
area, the resources necessary and the number of casualties or injuries is
predicted, and the number of volunteers are assigned to a disaster struck
are a accordingly

## News Headline Analytics for Disaster Prediction

Deep Learning based Natural Language Processing and Text Analytics
algorithms are used to analyse National News Headlines obtained from the
Bing News API and predict whether any kind of disaster has struck any part
of the country. Individuals from that region are sent a notification, and
queried whether they are safe. Individuals can mark themselves as safe or
under distress. The ones marked as safe have the option to register as
volunteers and if marked under distress, are marked as victims and relief
is notified immediately.

## Data Analytics of Disaster-Prone Areas

Disaster Heatmaps for various regions are generated through machine
learning and data analytics algorithms with users being notified what kind
of disasters are most probable in their locations and how probable it is.
Probability is calculated by applying regression models on factors like
weather conditions etc.

