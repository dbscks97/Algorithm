import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        int[] answer = {};
        HashMap<String, Integer> genres_sum = new HashMap<>();
        HashMap<String, HashMap<Integer, Integer>> music = new HashMap<>();
        
         for (int i = 0; i < plays.length; i++) {
            String genre = genres[i];
            int playCount = plays[i];
            
            genres_sum.put(genre, genres_sum.getOrDefault(genre, 0) + playCount);
            
            if (!music.containsKey(genre)) {
                music.put(genre, new HashMap<>());
            }
            music.get(genre).put(i, playCount);
        }
        List<String> genreOrder = new ArrayList<>(genres_sum.keySet());
        Collections.sort(genreOrder, (a, b) -> genres_sum.get(b) - genres_sum.get(a));
        
        List<Integer> bestAlbum = new ArrayList<>();
        for (String genre : genreOrder) {
            List<Map.Entry<Integer, Integer>> songs = new ArrayList<>(music.get(genre).entrySet());
            Collections.sort(songs, (a, b) -> b.getValue() - a.getValue());
            
            bestAlbum.add(songs.get(0).getKey());
            if (songs.size() > 1) {
                bestAlbum.add(songs.get(1).getKey());
            }
        }
        
        answer = bestAlbum.stream().mapToInt(i -> i).toArray();
        
        return answer;
    }
}