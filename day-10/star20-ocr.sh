#!/bin/bash

gcloud --format="value(responses[0].fullTextAnnotation.text)" ml vision detect-text star20.png
