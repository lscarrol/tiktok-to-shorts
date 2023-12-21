import TikTokScraper from 'tiktok-scraper';

(async () => {
 try {
     const posts = await TikTokScraper.hashtag('politics', {
         number: 100,
         sessionList: ['sid_tt=YOUR_SESSION_ID;']
     });

     posts.collector.sort((a: any, b: any) => b.stats.diggCount - a.stats.diggCount);

     const top5Posts = posts.collector.slice(0, 5);

     for (const post of top5Posts) {
         try {
             const video = await TikTokScraper.video(post.videoUrl, {
                download: true,
                filepath: 'YOUR_FILE_PATH',
                noWaterMark: true,
                headers: {
                   'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
                   referer: 'https://www.tiktok.com/',
                   cookie: `tt_webid_v2=YOUR_COOKIE;`,
                }
             });
             console.log(video);
         } catch (error) {
             console.log(error);
         }
     }
 } catch (error) {
     console.log(error);
 }
})();
