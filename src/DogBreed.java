package dog;

public class DogBreed {
    // Attributes
    private String name;
    private String picturePath;
    private String coat_colors;
    private String coat_pattern;
    private String coat_texture;
    private String ear_shape;
    private String Fun_Facts;
    private int weight_min;
    private int weight_max;
    private int muzzle_length_min;
    private int muzzle_length_max;
    private int leg_height_min;
    private int leg_height_max;

    // Getter
    public String getName() {
        return name;
    }

    public String getPicture() {
        return picturePath;
    }

    // Setter
    public void setName(String newName) {
        this.name = newName;
    }

    public void setWeightRange(int wmin, int wmax) {
        this.weight_min = wmin;
        this.weight_max = wmax;
    }

    public void setMuzzletRange(int mmin, int mmax) {
        this.muzzle_length_min = mmin;
        this.muzzle_length_max = mmax;
    }

    public void setHeightRange(int hmin, int hmax) {
        this.leg_height_min = hmin;
        this.leg_height_max = hmax;
    }

    public void setPicture(String path) {
        this.picturePath = path;
    }

    public DogBreed(String n, String p, String c, String x, String y, String z, int a, int b, int d, int e, int f,
            int g, String h) {
        this.name = n;
        this.picturePath = p;
        this.coat_colors = c;
        this.coat_pattern = x;
        this.coat_texture = y;
        this.ear_shape = z;
        this.weight_min = a;
        this.weight_min = b;
        this.muzzle_length_min = d;
        this.muzzle_length_max = e;
        this.leg_height_min = f;
        this.leg_height_max = g;
        this.Fun_Facts = h;
    }

}
