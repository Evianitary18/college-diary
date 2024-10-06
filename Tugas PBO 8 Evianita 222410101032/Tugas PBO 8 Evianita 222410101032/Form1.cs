namespace Tugas_PBO_8_Evianita_222410101032
{
    public partial class Form1 : Form
    {
        public string username = "Evi";
        public string password = "12345";
        public string no_hp = "0812332222219";
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void label3_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (textBox1.Text == username && textBox2.Text == password && textBox3.Text == no_hp)
            {
                Form2 form = new Form2();
                form.Show();
                this.Hide();
            }

        }

        private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            Form3 form = new Form3();
            form.Show();
            this.Hide();
        }
    }
}