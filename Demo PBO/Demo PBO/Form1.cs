using Demo_PBO.Controller;

namespace Demo_PBO
{
    public partial class Form1 : Form
    {
        Koneksi koneksi = new Koneksi();
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_load(Object sender, EventArgs e)
        {
            dataGridView1.DataSource = koneksi.showData(query: "SELECT * from nim");
        }
        private void groupBox1_Enter(object sender, EventArgs e)
        {

        }

        private void Form1_Load_1(object sender, EventArgs e)
        {

        }
    }
}