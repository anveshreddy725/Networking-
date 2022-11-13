import java.util.HashMap;
import java.util.Map;

public class nextHop {
    public static void BellmanFord(int n, int edges[][],int e,char V[], Map<Character,Integer> dis, int parent[]){
        int u,v,w;

        for(int i = 0; i<n-1; i++){
            for(int j = 0;j<e; j++){
                u = edges[j][0];
                v = edges[j][1];
                w = edges[j][2];
                if(dis.get(V[u]) + w < dis.get(V[v])){ 
                    dis.put(V[v],dis.get(V[u])+w);
                    parent[v] = u;
                }
            }
        }

        for(int j = 0; j<e; j++){
            u = edges[j][0];
            v = edges[j][1];
            w = edges[j][2];
            if(dis.get(V[v]) > dis.get(V[u])+w){
                System.out.println("Negative cycle detected");
                return;
            }
        }
        System.out.println("Source node : Number of hoops");

        for(int k = 0;k<n;k++){
            System.out.println(V[k] + " "+dis.get(V[k]));
            }
            System.out.println();
}
    public static void main(String[] args) {
        Map<Character, Integer> m = new HashMap<Character,Integer>();
        char V[] = {'u', 'v', 'x', 'w', 'y', 'z'};
        int parent[] = {-1,-1,-1,-1,-1,-1};
    
    for(int i = 0;i<6; i++){
        m.put(V[i],Integer.MAX_VALUE);
    }
    m.put('u', 0);
    int edges[][] = {{0,1,3},{0,2,1},{0,3,7},{1,2,1},{1,3,1},{2,4,2},{2,3,4},{3,4,5},{3,5,6},{4,5,3}};
    BellmanFord(6,edges,10,V,m,parent);
    }
}