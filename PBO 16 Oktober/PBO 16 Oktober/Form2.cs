using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace PBO_16_Oktober
{
    public partial class FormDataBaru : Form
    {
        public FormDataBaru()
        {
            InitializeComponent();
        }
        public Models.Mhs GetMahasiswaNew()
        {
            Models.Mhs newMahasiswa = new Models.Mhs();
            newMahasiswa.Nim = tbNIM.Text;
            newMahasiswa.Nama = tbNama.Text;
            newMahasiswa.Alamat = tbAlamat.Text;
            newMahasiswa.TglLahir = DateTime.Parse(dtpTglLahir.Value.ToShortDateString());
            newMahasiswa.KdProdi = ((Prodi)cbProdi.SelectedItem).KdProdi;
            newMahasiswa.NamaProdi = ((Prodi)cbProdi.SelectedItem).NamaProdi;
            newMahasiswa.UKT = decimal.Parse(tbUKT.Text);
            newMahasiswa.IsActive = chkIsActive.Checked;

            return newMahasiswa;


        }
      


            

        private void maskedTextBox1_MaskInputRejected(object sender, MaskInputRejectedEventArgs e)
        {

        }

        private void FormDataBaru_Load(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void maskedTextBox2_MaskInputRejected(object sender, MaskInputRejectedEventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }
    }
}
