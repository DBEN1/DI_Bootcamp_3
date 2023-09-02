class Video {
    constructor(title, uploader, time) {
        this.title = title;
        this.uploader = uploader;
        this.time = time;
    }

    watch() {
        return `${this.uploader} watched all ${this.time} seconds of ${this.title}!`;
    }
}
const video1 = new Video('My First Video', 'John', 120);
console.log(video1.watch());  // Outputs: John watched all 120 seconds of My First Video!
const video2 = new Video('My Second Video', 'Doe', 150);
console.log(video2.watch());  // Outputs: Doe watched all 150 seconds of My Second Video!
const videoData = [
    { title: 'Video A', uploader: 'Alice', time: 100 },
    { title: 'Video B', uploader: 'Bob', time: 200 },
    { title: 'Video C', uploader: 'Charlie', time: 300 },
    { title: 'Video D', uploader: 'David', time: 400 },
    { title: 'Video E', uploader: 'Eve', time: 500 }
];
const videoInstances = videoData.map(data => new Video(data.title, data.uploader, data.time));

// To watch all videos:
videoInstances.forEach(video => console.log(video.watch()));
