## Amazon Reviews: AI Detection & Analysis

This program is a web scraper to detect AI-generated reviews on Amazon. 

# How to use:
* initial setup * - clone repo and insert your API key in gptzero.py.
Run the main.py file.
Input amazon product page.
i.e. https://www.amazon.com/dp/B099N4NSSD (follow this format for url)
If captcha appears, manually complete. Then go back to the program and press “Enter”.
Wait for the “Scraping done” message, then check output files.

# Interesting results found:
For this example, we are going to use the “Projector with WiFi” product on Amazon. As of February 17 2024, this product has an overall rating of 4.4 stars with 3,356 ratings and 44 written reviews.

Our program tested each of these reviews with the GPTZero API to see if it would be classified as “AI”, “mixed”, or “human”. Out of 44 reviews, 8 were classified as “AI”, 6 of such having a high confidence score, 1 with a medium confidence score, and 1 having a low confidence score. Only one review was classified as “mixed” with a medium confidence score.

Interestingly, all of the reviews that were classified as “AI” were all 5 star reviews. While our dataset isn’t large enough for this to be a good judgment of much, I think it should be taken into consideration as AI assistance becomes more common in our everyday activities.

Here are some of the reviews that were classified as “AI”:

Predicted Class: ai
Confidence Score: 0.9447418104
Confidence Category: high

"After several weekends of movie nights in my backyard, I feel confident in sharing my thoughts on the 2023 Upgrade 9500L Outdoor Projector. Setting it up was a breeze; the instructions were clear, and I had it connected to my phone via WiFi in no time. The Bluetooth feature was just as seamless, allowing me to enhance the audio with my external speakers effortlessly.

The picture quality is impressive for its price point. The 1080P resolution delivers clear and vibrant images, and the 9500 lumens of brightness make evening screenings a delight, even with some ambient light. The focus and keystone correction features are straightforward, allowing for a crisp image on my makeshift screen.

The built-in speakers are decent, but for the full cinematic experience, I recommend pairing it with a quality outdoor speaker system, especially if you're like me, who enjoys the rumble of bass during action scenes.

In terms of build, it feels sturdy and portable, though I wouldn't risk leaving it outside overnight. It's lightweight enough to move around but doesn't feel fragile. The design is sleek and modern, with intuitive controls on the projector itself and a handy remote control.

One of the standout features for me is the ability to synchronize my smartphone screen. It's incredibly convenient for streaming from apps that aren't natively supported by the projector's system. The WiFi connection has been stable, and I haven't experienced any lag or disconnection issues during streaming.

I haven't had to worry about battery life since it's a plug-in model, which is perfect for my setup where I have easy access to an outdoor outlet. Power consumption seems efficient, as I haven't noticed any significant increase in my electricity bill.

Finally, I haven't had the need to contact customer service, which in itself is a testament to the product's quality and user-friendliness. But I did register the product online and received a confirmation email promptly, which gives me confidence in their customer service responsiveness.

For the price, this projector has exceeded my expectations. It's a fantastic option for anyone looking to enjoy their favorite films under the stars. Whether it's a family night or a gathering of friends, this projector has definitely been the highlight of the evening."




Predicted Class: ai
Confidence Score: 0.9427693367
Confidence Category: high

"I recently purchased the WiFi Projector from this listing and, so far, I must say it's been a superb addition to our family movie nights. I was in the market for a budget-friendly projector that would offer good quality and a decent brightness level without breaking the bank - this one has more than delivered on that.

First and foremost, the brightness on this projector is a standout feature. It's significantly brighter than other projectors I considered in a similar price range. The vividness and clarity make it an absolute joy to use in a dimly lit room. However, it's important to note that this isn't a high-end projector - if you're looking for cinema-level image quality, you might need to invest a little more. Yet, for a fun, family-oriented device to enjoy movies, this projector is a gem.

As for the quality, it's surprisingly good given the price point. The projected image is clear and color reproduction is quite decent. I would stress that it's necessary to have a good screen or a white wall to get the best results. It's an inexpensive option that offers a good balance between quality and price, perfect for those who are just venturing into the world of home projectors.

In terms of connectivity, I've mainly used the HDMI and USB ports to connect my devices. Both have worked flawlessly, with a seamless connection and no lag or interruption in video playback. While I haven't tried out the WiFi connectivity yet, it's a feature that could come in handy for those who prefer wireless streaming.

The build of the projector itself is sturdy and compact, easy to set up and use, which makes it ideal for those who aren't too tech-savvy. The included instructions were clear and made the setup process straightforward.

In conclusion, if you're seeking a budget-friendly projector that delivers good quality and brightness for your family movie nights, this one fits the bill nicely. It offers excellent value for the price and is a solid performer in its class. Just remember that it's not competing with top-tier projectors, and you won't be disappointed.

Overall, I'm satisfied with this purchase and would recommend it to others looking for a fun, affordable home cinema experience."

More results can be found on the GitHub or this google sheet.
