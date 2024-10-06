namespace Tugas_PBO_Pertemuan_8
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

            dataGridView1.Columns.Add("Nomor", "Nomor");
            dataGridView1.Columns.Add("Nama", "Nama");
            dataGridView1.Columns.Add("Tumbuhan", "Tumbuhan");
            dataGridView1.Columns.Add("Jenis", "Habitat");
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {

        }
    }
}