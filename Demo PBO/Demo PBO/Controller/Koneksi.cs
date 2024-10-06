using System;
using System.Collections.Generic;
using System.ComponentModel.Design;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Npgsql;
using System.Data;

namespace Demo_PBO.Controller
{
    class Koneksi
    {
        string constr = "Host=localhost;Port=4321;Database=Surat_Tugas_Dospem; User Id=postgres; Password=123"
        NpgsqlConnection con;

        public void openConnection()
        {
            con = new NpgsqlConnection(conStr);

        }
        public void closeConnection() 
        {
            con.Close();
        }

        public void executyQuery()
        {
            NpgsqlComand cmd = new NpgsqlComand(Queryable, con);
            cmd.ExecuteNonQuery();
        }

        public object showData(string query)
        { 
            NpgsqlDataAdapter adapter = new NpgsqlDataAdapter(query, conStr);
            DataSet dataset = new DataSet();
            adapter.Fill(dataset);
            object entity = dataset.Tables[0];

        }
    }
}
