This tool is a proxies based botnet which is using the proxies as bots to take down any target, and this is the one that took down YouTube on or more than 1 hours using a good VPS!!!

what make this tool different of others similar tools are:

-bots number (minimum: 20k, maximum: 43k) -fast proxies -tactic used: it picks up randomly 70 to 80 unique proxies of those thousands and uses them for flooding for a small interval between 30 to 60 seconds to prevent IP blocking for the bots and not exhausting them to keep the attack speed at it max always -methods of attack: it uses 2 methods unlike the others: simple GET and POST using large strings between 1000 and 3000 characters with "search" keyword which pushes the server to make a long process to search for the posted data on their database. -library used for connection between your machine and the bots: httplib is the fastest here (more than socket and others) cuz all we need to do is:

connecting to proxy=>send http request=>proxy pass the request to the target=> server return response=> proxy receives the response but we never receive any data from the proxy

so all we are doing here is sending through proxies but never receive anything, while the proxies are the ones who passes the requests but receive the data every time.

why am I using proxies?

-make the attack distributed and bypass geo restriction -limit the requests sent per IP -hide our real IP (although some are transparent proxies but it doesn't matter since they are few ones and the attack is distributed over thousands of others)

what do I need to use it?

-install the dependencies: requests bs4 



-any computer or phone could be used but for big targets it's highly recommended to use a VPS like we did on our test on YouTube.

enjoy your time using this tool :) ;).
