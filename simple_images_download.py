from simple_images_download import simple_images_download as simp
response = simp.simple_images_download
keywords = ["No Foam","Foam","Grid","wall"]
for kw in keywords:
    response().download(kw,200)